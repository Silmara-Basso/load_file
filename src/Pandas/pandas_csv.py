
import pandas as pd
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

CONCURRENCY = cpu_count()

total_rows = 1000000000
chunk_size = 100000000
file_name = "data/weather_stations.csv"


def process_chunk(chunk):
    # Aggregate data with Pandas
    aggregated = chunk.groupby('station')['measure'].agg(['min', 'max', 'mean']).reset_index()
    return aggregated

def create_df_with_pandas(file_name, total_rows, chunk_size):
    total_chunks = total_rows // chunk_size + (1 if total_rows % chunk_size else 0)
    results = []

    with pd.read_csv (file_name, sep=';', header=None, names=['station', 'measure'], chunksize=chunk_size) as reader:
        # tqdm to visualise the progress
        with Pool(CONCURRENCY) as pool:
            for chunk in tqdm(reader, total=total_chunks, desc="Processing"):
                # Process each chunk in parallel
                result = pool.apply_async(process_chunk, (chunk,))
                results.append(result)

            results = [result.get() for result in results]

    final_df = pd.concat(results, ignore_index=True)

    final_aggregated_df = final_df.groupby('station').agg({
        'min': 'min',
        'max': 'max',
        'mean': 'mean'
    }).reset_index().sort_values('station')

    return final_aggregated_df

if __name__ == "__main__":
    import time

    print("Iniciando o processamento do arquivo.")
    start_time = time.time()
    df = create_df_with_pandas(file_name, total_rows, chunk_size)
    took = time.time() - start_time

    print(df.head())
    print(f"Processing took: {took:.2f} sec")