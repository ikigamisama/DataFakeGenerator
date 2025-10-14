import csv
import json
from pathlib import Path


class Exporter:

    @staticmethod
    def to_csv(data: list[dict], file_path: str):
        if not data:
            raise ValueError("No data to export.")
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"CSV saved to: {file_path}")

    @staticmethod
    def to_json(data: list[dict], file_path: str):
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"JSON saved to: {file_path}")

    @staticmethod
    def to_sql(data: list[dict], table_name: str, file_path: str, create_table: bool):
        if not data:
            raise ValueError("No data to export.")
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        columns = ", ".join(data[0].keys())

        def format_sql_value(v):
            """Return a SQL-safe literal for Python value v."""
            if v is None:
                return "NULL"
            if isinstance(v, bool):
                return "TRUE" if v else "FALSE"
            if isinstance(v, (int,)) and not isinstance(v, bool):
                return str(v)
            if isinstance(v, float):
                return repr(v)
            s = str(v)
            return "'" + s.replace("'", "''") + "'"

        first_row = data[0]
        type_map = {}
        for col, val in first_row.items():
            if isinstance(val, bool):
                type_map[col] = "BOOLEAN"
            elif isinstance(val, int) and not isinstance(val, bool):
                type_map[col] = "INTEGER"
            elif isinstance(val, float):
                type_map[col] = "REAL"
            elif val is None:
                type_map[col] = "TEXT"
            else:
                type_map[col] = "TEXT"

        with open(file_path, "w", encoding="utf-8") as f:
            if create_table:
                cols_def = ",\n    ".join(
                    f"{col} {type_map[col]}" for col in columns)
                f.write(
                    f"CREATE TABLE IF NOT EXISTS {table_name} (\n    {cols_def}\n);\n\n")

            cols_str = ", ".join(columns)
            for row in data:
                values = ", ".join(format_sql_value(row.get(col))
                                   for col in columns)
                f.write(
                    f"INSERT INTO {table_name} ({cols_str}) VALUES ({values});\n")

        print(f"SQL file saved to: {file_path}")
