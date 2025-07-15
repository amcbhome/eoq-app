# EOQ Calculator (ACCA Example 1)

This Streamlit app calculates Economic Order Quantity (EOQ) based on the ACCA F2 technical article example.

### Formula
EOQ = √(2DCₒ / Cₕ)

Where:
- D = Annual demand (units)
- Cₒ = Ordering cost per order (£)
- Cₕ = Holding cost per unit per year (£)

### Example
- Annual demand: 32,000 units
- Ordering cost: £25
- Holding cost: £1.50
- **EOQ = 1,637 units**

### Run the App
```bash
streamlit run eoq_model.py
