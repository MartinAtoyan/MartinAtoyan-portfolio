def info_about_car(brand, model, year, odometer):
    print(f"Brand: {brand}") 
    print(f"Model: {model}")
    print(f"Year: {year}")
    print(f"Odometer: {odometer}")
    
di = {
    "brand": "BMW",
    "model": "5 series",
    "year": 2023,
    "odometer": "1024 km"
}

info_about_car(**di)
