class SalesAnalyzer:

    def __init__(self, data):
        self.data = data

    def calculate_basic_stats(self):
        """Calculate basic sales statistics."""

        if self.data is None or self.data.empty:
            return None

        stats = {
            "total_sales": self.data["total_amount"].sum(),
            "average_order_value": self.data["total_amount"].mean(),
            "total_orders": self.data["order_id"].nunique(),
            "unique_customers": self.data["customer_id"].nunique(),
            "unique_products": self.data["product_id"].nunique()
        }

        return stats

    def sales_by_category(self):
        """Calculate total sales by product category."""

        category_sales = (
            self.data.groupby("category")["total_amount"]
            .sum()
            .sort_values(ascending=False)
        )

        return category_sales

    def top_products(self, limit=5):
        """Find the top selling products by total sales."""

        product_sales = (
            self.data.groupby("product_name")["total_amount"]
            .sum()
            .sort_values(ascending=False)
            .head(limit)
        )

        return product_sales

    def monthly_sales_trends(self):
        """Calculate monthly sales totals and growth rates."""

        monthly_sales = (
            self.data.groupby(
                self.data["order_date"].dt.to_period("M")
            )["total_amount"]
            .sum()
            .to_frame(name="total_sales")
        )

        monthly_sales["growth_rate"] = (
            monthly_sales["total_sales"]
            .pct_change() * 100
        )

        return monthly_sales

    def peak_sales_month(self):
        """Find the month with the highest sales."""

        monthly_sales = self.monthly_sales_trends()

        if monthly_sales.empty:
            return None

        peak_month = monthly_sales["total_sales"].idxmax()
        peak_sales = monthly_sales["total_sales"].max()

        return peak_month, peak_sales

    def customer_analysis(self):
        """Analyze customer purchase patterns."""

        customer_sales = (
            self.data.groupby("customer_id")
            .agg(
                total_spent=("total_amount", "sum"),
                total_orders=("order_id", "nunique")
            )
            .sort_values("total_spent", ascending=False)
        )

        return customer_sales

    def sales_by_region(self):
        """Calculate total sales by geographical region."""

        region_sales = (
            self.data.groupby("region")["total_amount"]
            .sum()
            .sort_values(ascending=False)
        )

        return region_sales

    def moving_average_forecast(self, window=3):
        """Calculate a simple moving average of monthly sales."""

        monthly_sales = self.monthly_sales_trends().copy()

        monthly_sales["moving_average"] = (
            monthly_sales["total_sales"]
            .rolling(window=window)
            .mean()
        )

        return monthly_sales