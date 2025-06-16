from admit.models import Payment

def financial_summary(request):
    """
    View to display financial summary of payments.
    """
    payments = Payment.objects.all()
    total_payments = payments.count()
    total_amount = sum(payment.ammount for payment in payments)

    context = {
        'payments': payments,
        'total_payments': total_payments,
        'total_amount': total_amount,
    }
    
    return context
