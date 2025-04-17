from pet import Pet

# Create a new pet named Max
max_pet = Pet("Max")

# Test the functionality
max_pet.eat()
max_pet.play()
max_pet.sleep()

# Get the current status
max_pet.get_status()

# Teach Max a new trick and show tricks
max_pet.train("roll over")
max_pet.train("play dead")
max_pet.show_tricks()

# Show the final status
max_pet.get_status()
