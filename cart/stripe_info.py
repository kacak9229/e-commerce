secret_key = 'sk_test_QUglzw1h3lzKNY7Lwma4avB9'
publishable_key = 'pk_test_AdGaWGZMGREkdovLS4TYsOVk'

stripe.Charge.create(
  amount=800000,
  currency="usd",
  card="tok_2J89xYi3UYD4qA", # obtained with Stripe.js
  description="Charge for test@example.com"
)

"cus_2J8JamjQZNWMl0"