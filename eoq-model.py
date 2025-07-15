# eoq_model.py

import math
import streamlit as st

def calculate_eoq(demand, ordering_cost, holding_cost):
    """Calculate Economic Order Quantity (EOQ)."""
    return math.sqrt((2 * demand * ordering_cost) / holding_cost)

def main():
    st.set_page_config(page_title="EOQ Calculator", layout="centered")
    st.title("📦 EOQ (Economic Order Quantity) Calculator")

    st.markdown("This app calculates the optimal order quantity using the classic EOQ model.")
    st.markdown("**Formula:** $EOQ = \\sqrt{\\frac{2DC_o}{C_h}}$")

    st.markdown(
        """
        ---
        📖 **Reference**: This EOQ model is based on **Example 1** from the ACCA technical article  
        👉 [Stock Control – Economic Order Quantity (EOQ)](https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f2/technical-articles/stock-control.html)

        🎓 It forms part of the **Management Accounting syllabus** (ACCA F2 / MA), covering inventory control techniques and cost optimization.
        """
    )

    with st.form("eoq_form"):
        demand = st.number_input("Annual Demand (units)", min_value=1, value=32000)
        ordering_cost = st.number_input("Ordering Cost per Order (£)", min_value=0.01, value=25.0)
        holding_cost = st.number_input("Holding Cost per Unit per Year (£)", min_value=0.01, value=1.5)

        submitted = st.form_submit_button("Calculate EOQ")

        if submitted:
            eoq = calculate_eoq(demand, ordering_cost, holding_cost)
            st.success(f"✅ EOQ: {eoq:.2f} units")
            total_orders = demand / eoq
            st.info(f"📦 Expected number of orders per year: {total_orders:.1f}")

if __name__ == "__main__":
    main()
