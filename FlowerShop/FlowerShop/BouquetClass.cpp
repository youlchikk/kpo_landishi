#include "BouquetClass.h"

BouquetClass::BouquetClass(std::string name_Bouquet, std::string buyer, std::vector<FlowerClass*> flowers) {
	name = name_Bouquet;
	buyer_name = buyer;
	massBouquet = 0;
	price = 0;
	for (int i = 0; i < flowers.size(); i++) {
		massBouquet += flowers[i]->mass;
		price += flowers[i]->price;
	}
	flowers_Bouquet = flowers;
	std::cout << "Создан букет " << name << " стоимостью " << price << " и массой " << massBouquet << std::endl;
}

double BouquetClass::MinimumFlower() {
	double minimum = 2e9;
	int j = 0;
	for (int i = 0; i < flowers_Bouquet.size(); i++) {
		if (flowers_Bouquet[i]->price < minimum) {
			minimum = flowers_Bouquet[i]->price;
			j = i;
		}
	}
	std::cout << "Минимальный по стоимости цветок в букете " << flowers_Bouquet[j]->name << " стоимостью " << minimum << std::endl;
	return minimum;
}

double BouquetClass::MaximumFlower() {
	double maximum = 0;
	int j = 0;
	for (int i = 0; i < flowers_Bouquet.size(); i++) {
		if (flowers_Bouquet[i]->price > maximum) {
			maximum = flowers_Bouquet[i]->price;
			j = i;
		}
	}
	std::cout << "Максимальный по стоимости цветок в букете " << flowers_Bouquet[j]->name << " стоимостью " << maximum << std::endl;
	return maximum;
}

double BouquetClass::getMassBouquet() {
	return massBouquet;
}

double BouquetClass::getPriceBouquet() {
	return price;
}