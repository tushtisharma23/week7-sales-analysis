import pandas as pd


class DataLoader:

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """Load sales data from CSV or Excel file."""

        try:
            if self.file_path.endswith(".csv"):
                self.data = pd.read_csv(self.file_path)

            elif self.file_path.endswith((".xlsx", ".xls")):
                self.data = pd.read_excel(self.file_path)

            else:
                print("Unsupported file format.")
                return None

            print("\nData loaded successfully!")
            print(f"Rows: {self.data.shape[0]}")
            print(f"Columns: {self.data.shape[1]}")

            return self.data

        except FileNotFoundError:
            print("Error: Data file not found.")
            return None

        except Exception as error:
            print(f"Error loading data: {error}")
            return None

    def show_basic_info(self):
        """Display basic information about the dataset."""

        if self.data is None:
            print("No data loaded.")
            return

        print("\n===== DATASET INFORMATION =====")
        print(f"Total Rows: {len(self.data)}")
        print(f"Total Columns: {len(self.data.columns)}")

        print("\nColumn Names:")
        for column in self.data.columns:
            print(f"- {column}")

        print("\nMissing Values:")
        print(self.data.isnull().sum())

        print("\nData Types:")
        print(self.data.dtypes)

        print("\nFirst 5 Records:")
        print(self.data.head())