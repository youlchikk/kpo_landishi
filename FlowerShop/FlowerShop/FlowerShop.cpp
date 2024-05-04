#include <iostream>
#include "FlowerShopClass.h"
#include "BouquetClass.h"
#include "FlowerClass.h"
#include <vector>

std::vector<int> convert_to_array();

int main()
{
	setlocale(LC_ALL, "Russian");
	FlowerShopClass *shop = new FlowerShopClass("Ландыши", 5.1);
	shop->Add_Flower(new FlowerClass("ландыши", 6.99, 0.09, 20));
	shop->Add_Flower(new FlowerClass("ромашки", 3.99, 0.05, 35));
	shop->Add_Flower(new FlowerClass("пионы", 8.99, 0.08, 15));
	shop->Add_Flower(new FlowerClass("розы", 5.99, 0.11, 20));
	shop->Add_Flower(new FlowerClass("лилии", 12.99, 0.13, 25));
	shop->Add_Flower(new FlowerClass("гипсофила", 12.99, 0.13, 25));
	shop->Print_Flower();
	std::vector <int> list = convert_to_array();
	std::vector <FlowerClass*> list_flowers = shop->Array_of_flowers_creat(list);
	BouquetClass *bouquet = new BouquetClass("букетик", "student", list_flowers);
	bouquet->MaximumFlower();
	bouquet->MinimumFlower();
}


std::vector<int> convert_to_array() {
	std::cout << "Введите номеры цветов, которые будут в букете\n";
	std::string s;
	getline(std::cin, s);
	s += ' ';
	std::vector <int> list;
	int x = 0;
	int i = 0;
	while (i < s.length()) {
		int j = i;
		while (s[j] != ' ') {
			x = x * 10 + (s[j] - '0');
			j++;
		}
		list.push_back(x - 1);
		x = 0;
		i = j + 1;
	}
	return list;
}