from sales_analyzer.data_loader import DataLoader
from sales_analyzer.data_cleaner import DataCleaner
from sales_analyzer.analyzer import SalesAnalyzer
from sales_analyzer.visualizer import SalesVisualizer
from sales_analyzer.reporter import SalesReporter


class SalesAnalysisSystem:

    def __init__(self):
        self.data_path = "data/raw/sales_data.csv"
        self.data = None
        self.analyzer = None
        self.visualizer = None
        self.reporter = None

    def setup(self):
        """Load and clean the sales data."""

        loader = DataLoader(self.data_path)
        self.data = loader.load_data()

        if self.data is None:
            return False

        cleaner = DataCleaner(self.data)
        self.data = cleaner.clean_data()

        if self.data is None:
            return False

        cleaner.save_cleaned_data()

        self.analyzer = SalesAnalyzer(self.data)
        self.visualizer = SalesVisualizer(self.analyzer)
        self.reporter = SalesReporter(self.analyzer)

        return True

    def show_basic_statistics(self):
        """Display key sales statistics."""

        stats = self.analyzer.calculate_basic_stats()

        print("\n" + "=" * 50)
        print("           BASIC SALES STATISTICS")
        print("=" * 50)

        print(f"Total Sales         : Rs. {stats['total_sales']:,.2f}")
        print(f"Total Orders        : {stats['total_orders']}")
        print(
            f"Average Order Value : "
            f"Rs. {stats['average_order_value']:,.2f}"
        )
        print(f"Unique Customers    : {stats['unique_customers']}")
        print(f"Unique Products     : {stats['unique_products']}")

        print("=" * 50)

    def show_category_analysis(self):
        """Display sales by category."""

        print("\n===== SALES BY CATEGORY =====")
        print(self.analyzer.sales_by_category())

    def show_top_products(self):
        """Display the top selling products."""

        print("\n===== TOP 5 PRODUCTS =====")
        print(self.analyzer.top_products())

    def show_monthly_trends(self):
        """Display monthly sales trends."""

        print("\n===== MONTHLY SALES TRENDS =====")
        print(self.analyzer.monthly_sales_trends())

    def show_customer_analysis(self):
        """Display customer purchase analysis."""

        print("\n===== CUSTOMER ANALYSIS =====")
        print(self.analyzer.customer_analysis())

    def show_menu(self):
        """Display the main application menu."""

        print("\n" + "=" * 55)
        print("             SALES DATA ANALYSIS SYSTEM")
        print("=" * 55)

        print("1. View Basic Statistics")
        print("2. View Sales by Category")
        print("3. View Top Products")
        print("4. View Monthly Sales Trends")
        print("5. View Customer Analysis")
        print("6. Generate Visualizations")
        print("7. Generate Reports")
        print("8. Generate All Visualizations and Reports")
        print("0. Exit")

        print("=" * 55)

        return input("Enter your choice: ")

    def run(self):
        """Run the sales analysis application."""

        print("\nLoading Sales Analysis System...")

        if not self.setup():
            print("Unable to start the application.")
            return

        print("\nSales data is ready for analysis!")

        while True:

            choice = self.show_menu()

            if choice == "1":
                self.show_basic_statistics()

            elif choice == "2":
                self.show_category_analysis()

            elif choice == "3":
                self.show_top_products()

            elif choice == "4":
                self.show_monthly_trends()

            elif choice == "5":
                self.show_customer_analysis()

            elif choice == "6":
                self.visualizer.create_all_visualizations()

            elif choice == "7":
                self.reporter.generate_all_reports()

            elif choice == "8":
                self.visualizer.create_all_visualizations()
                self.reporter.generate_all_reports()

            elif choice == "0":
                print("\nThank you for using Sales Data Analysis System!")
                break

            else:
                print("\nInvalid choice! Please try again.")


def main():

    app = SalesAnalysisSystem()
    app.run()


if __name__ == "__main__":
    main()