import streamlit

def calculate_emi(p, n, r):
	emi = p * (r/100) * (1 + (r/100) ** n) / ((1 + r/100)** n - 1)
	st.write("EMI Calculator = ", round(emi, 3))
st.title("EMI Calculator ")

principal = st.slider("Loan Ammount ", 1000.0, 100000.0)
tenure = st.slider("Tenure in years ", 1, 30)
roi = st.slider("Intrest Rate ", 1, 50)

n = tenure * 12
r = roi / 12
if st.button("Calculate "):
	calculate_emi(principal, n, r)