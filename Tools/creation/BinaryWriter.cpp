#include <iostream>
#include <filesystem>
#include <fstream>


int main(int argc, char const *argv[])
{

    std::ofstream outfile("out.bin", std::ofstream::binary);
    if (!outfile)
	{
		std::cout << "can't open file" << std::endl;
		exit(1);
	}
    std::string str("whatever");
    auto size = str.size();
    outfile.write(reinterpret_cast<char * >(&size),sizeof(size));
    outfile.write(str.c_str(), size);

    std::ifstream infile("out.bin", std::ifstream::binary);
	if (!infile)
	{
		std::cout << "can't open file" << std::endl;
		exit(1);
	}

	infile.read(reinterpret_cast<char *>(&size), sizeof(size));
	infile.read(reinterpret_cast<char *>(&str), size);

    
    return 0;
}
