document.getElementById('btnClick').addEventListener('click', submitForm);

async function submitForm() {
    try {
        const response = await fetch('/create_payment_link', { method: 'POST' });
        const payment = await response.json();
        window.open(payment.checkoutUrl);
    } catch (error) {
        console.error('Error:', error);
    }
}
