from django.contrib.auth import views as auth_views

urlpatterns = [
    # Запит на скидання паролю (користувач вводить email)
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    # Повідомлення про відправку email
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    
    # Сторінка для введення нового пароля (перехід з email)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # Повідомлення про успішне оновлення пароля
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
