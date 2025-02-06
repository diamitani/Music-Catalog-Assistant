import pandas as pd

def generate_catalog(metadata_list, output_format='csv'):
    df = pd.DataFrame(metadata_list)
    output_file = f"music_catalog.{output_format}"
    
    if output_format == 'csv':
        df.to_csv(output_file, index=False)
    elif output_format == 'excel':
        df.to_excel(output_file, index=False)
    elif output_format == 'json':
        df.to_json(output_file, orient='records')
    else:
        raise ValueError("Unsupported output format")
    
    return output_file
