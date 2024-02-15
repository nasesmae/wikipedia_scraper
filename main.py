from src.scraper import get_leaders, save

leaders_per_country = get_leaders()
print(leaders_per_country)
save(leaders_per_country)