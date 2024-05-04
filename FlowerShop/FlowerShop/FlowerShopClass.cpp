#include "FlowerShopClass.h"


FlowerShopClass::FlowerShopClass(std::string name_shop = "FlowerShop", double star_shop = 5) {
	name = name_shop;
	stars = star_shop;
	std::cout << "Создан магазин цветов с названием " << name << " и рейтингом " << stars << std::endl;
}

void FlowerShopClass::Add_Flower(FlowerClass* flower) {
	flowers.push_back(flower);
}

void FlowerShopClass::Print_Flower() {
	std::cout << "В магазине цветом есть такие цветы, как: \n";
	for (int i = 0; i < flowers.size(); i++) {
		std::cout << i + 1 << ") " << flowers[i]->name << " стоимостью " << flowers[i]->price << " и массой " << flowers[i]->mass << std::endl;
	}
}

std::vector <FlowerClass*> FlowerShopClass::Array_of_flowers_creat(std::vector <int> numbers) {
	std::vector <FlowerClass*> flowers_new;
	for (int i = 0; i < numbers.size(); i++) {
		flowers_new.push_back(flowers[i]);
	}
	return flowers_new;
}