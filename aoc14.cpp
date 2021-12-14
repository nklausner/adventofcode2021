#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>


//BCFHKNOPSV


std::string pair[100] = {"  "};
unsigned long long paircount[100] = {0};
unsigned long long pairdiff[100] = {0};
std::string pairone[100] = {"  "};
std::string pairtwo[100] = {"  "};
unsigned long long indexone[100] = {0};
unsigned long long indextwo[100] = {0};


std::vector<std::string> read_file(std::string myfilename)
{
    std::vector<std::string> myvec;
    std::string myline;
    std::ifstream myfile;
    std::string mypath = "./input/" + myfilename;
    myfile.open(mypath);
    while(!myfile.eof())
    {
        std::getline(myfile, myline);
        myvec.push_back(myline);
    }
    myfile.close();
    return myvec;
}


void define_pairs(std::vector<std::string>& myvec)
{
    unsigned i = 0;
    for(std::string& s : myvec)
    {
        if (s.size() == 7 && i < 100)
        {
            pair[i] = s.substr(0,2);
            pairone[i] = s.substr(0,1) + s.substr(6,1);
            pairtwo[i] = s.substr(6,1) + s.substr(1,1);
            // std::cout << pair[i] + " ";
            // std::cout << pairone[i] + " ";
            // std::cout << pairtwo[i] << std::endl;
            i++;
        }
    }
}


void set_index_references()
{
    for(unsigned i = 0; i < 100; i++)
    {
        if (pair[i] != " ")
        {
            for(unsigned j = 0; j < 100; j++)
            {
                if (pairone[i] == pair[j]) {
                    indexone[i] = j;
                }
                if (pairtwo[i] == pair[j]) {
                    indextwo[i] = j;
                }
            }
            // std::cout << pair[i] + " ";
            // std::cout << indexone[i];
            // std::cout << " ";
            // std::cout << indextwo[i] << std::endl;
        }
    }
}


void initialize_pair_counts(std::string& mystr)
{
    for(unsigned i = 0; i < mystr.size() - 1; i++)
    {
        for(unsigned j = 0; j < 100; j++)
        {
            if (mystr.substr(i, 2) == pair[j])
            {
                paircount[j]++;
                break;
            }
        }
        //std::cout << mystr.substr(i, 2) << std::endl;
    }
}


void excute_polymerization_step(int step)
{
    unsigned long long n = 0;
    for (unsigned i = 0; i < 100; i++)
    {
        if (paircount[i] > 0) {
            pairdiff[indexone[i]] += paircount[i];
            pairdiff[indextwo[i]] += paircount[i];
            pairdiff[i] -= paircount[i];
        }
    }
    for (unsigned i = 0; i < 100; i++)
    {
        if (pairdiff[i] != 0) {
            paircount[i] += pairdiff[i];
            pairdiff[i] = 0;
        }
        n += paircount[i];
    }
    std::cout << step + 1 << " " << n << std::endl;
}


void print_pair_count()
{
    unsigned long long n = 0;
    for (unsigned i = 0; i < 16; i++)
    {
        std::cout << pair[i] + " ";
        std::cout << paircount[i] << std::endl;
        n += paircount[i];
    }
    std::cout << "total number: " << n << std::endl;
}


void print_element_count(std::string mystart)
{
    std::string elements = "BCFHKNOPSV";
    unsigned long long counts[10] = {0};
    std::cout << " " << std::endl;

    for (unsigned i = 0; i < 100; i++)
    {
        char c = pair[i][0];
        std::size_t x = elements.find(c);
        if (x <= 10) {
            counts[x] += paircount[i];
        }
    }
    char c = mystart.back();
    std::size_t x = elements.find(c);
    if (x <= 10) { counts[x]++; }

    for (unsigned i = 0; i < 10; i++)
    {
        std::cout << elements[i] << " " << counts[i] << std::endl;
    }

    std::sort(counts, counts+10);
    std::cout << "The difference: " << counts[9] - counts[0] << std::endl;
}


int main()
{
    //calculating the exponential growth of the polymer chain

    std::vector<std::string> myinput = read_file("input14.txt");
    define_pairs(myinput);
    initialize_pair_counts(myinput.at(0));
    set_index_references();

    for(unsigned i = 0; i < 40; i++) {
        excute_polymerization_step(i);
    }

    print_element_count(myinput.at(0));
}