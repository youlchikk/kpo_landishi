#include "FlowerShopClass.h"


FlowerShopClass::FlowerShopClass(std::string name_shop = "FlowerShop", double star_shop = 5) {
	name = name_shop;
	stars = star_shop;
	std::cout << "������ ������� ������ � ��������� " << name << " � ��������� " << stars << std::endl;
}

void FlowerShopClass::Add_Flower(FlowerClass* flower) {
	flowers.push_back(flower);
}

void FlowerShopClass::Print_Flower() {
	std::cout << "� �������� ������ ���� ����� �����, ���: \n";
	for (int i = 0; i < flowers.size(); i++) {
		std::cout << i + 1 << ") " << flowers[i]->name << " ���������� " << flowers[i]->price << " � ������ " << flowers[i]->mass << std::endl;
	}
}

std::vector <FlowerClass*> FlowerShopClass::Array_of_flowers_creat(std::vector <int> numbers) {
	std::vector <FlowerClass*> flowers_new;
	for (int i = 0; i < numbers.size(); i++) {
		flowers_new.push_back(flowers[i]);
	}
	return flowers_new;
}