#include <iostream>
#include <fstream>
#include <string>
#include <vector>


int size = 500;
int myarray[500][500] = {0};
int myflood[500][500] = {0};
int myfloodcap = 3000;
unsigned long long visited = 0;
//std::string mytrack[100] = {""};


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


void fill_array(std::vector<std::string>& myvec)
{
    for (int y = 0; y < size; y++) {
        for (int x = 0; x < size; x++)
        {
            int h = (int)myvec[y][x] - 48;
            myarray[y][x] = h;
            myflood[y][x] = myfloodcap;
            //std::cout << h << std::endl;
        }
        //std::string myline(size, '.');
        //mytrack[y] = myline;
    }
}


void fill_array_times_five(std::vector<std::string>& myvec)
{
    int smallsize = size / 5;
    int xs = 0;
    int ys = 0;
    int h = 0;
    int d = 0;

    for (int y = 0; y < size; y++) {
        for (int x = 0; x < size; x++)
        {
            xs = x % smallsize;
            ys = y % smallsize;
            d = x / smallsize + y / smallsize;
            h = (int)myvec[ys][xs] - 48 + d;
            h = (h > 9) ? h - 9 : h;
            myarray[y][x] = h;
            myflood[y][x] = myfloodcap;
            //std::cout << h;
        }
        //std::cout << "" << std::endl;
    }
}


// void print_track()
// {
//     for (std::string& s : mytrack) {
//         std::cout << s << std::endl;
//     }
// }


int sum_next(int n, int x, int y)
{
    int s = myarray[y][x];

    if (n == 1) {
        return s;
    }
    else if (x == size - 1) {
        for (int i = 1; i < n; i++) {
            s += myarray[y+i][x];
        }
        return s;
    }
    else if (y == size - 1) {
        for (int i = 1; i < n; i++) {
            s += myarray[y][x+i];
        }
        return s;
    }
    else if (sum_next(n-1, x, y+1) < sum_next(n-1, x+1, y)) {
        return s + sum_next(n-1, x, y+1);
    }
    else {
        return s + sum_next(n-1, x+1, y);
    }
    return s;
}


void find_path_looking_ahead(int nmax)
{
    if (nmax == 0) {
        std::cout << "cant find path with step 0" << std::endl;
        return;
    }
    int x = 0;
    int y = 0;
    int s = 0;
    for (int i = 0; i < 2 * size - 2; i++)
    {
        if (x == size - 1) {
            y++;
            //std::cout << "forced";
        }
        else if (y == size - 1) {
            x++;
            //std::cout << "forced";
        }
        else {
            int rest = 2 * size - 2 - i;
            int n = (nmax > rest) ? rest : nmax;

            int sdown = sum_next(n, x, y+1);
            int sright = sum_next(n, x+1, y);

            if (sdown < sright) {
                y++;
                //std::cout << sdown << " down ";
            }
            else {
                x++;
                //std::cout << sright << " right ";
            }
        }
        s += myarray[y][x];
        //mytrack[y][x] = 'X';
        //std::cout << myarray[y][x] << std::endl;
    }
    std::cout << nmax << " sum: " << s << std::endl;
}


void flood_fill(int x, int y, int s)
{
    if (x >= 0 && x < size &&
        y >= 0 && y < size)
    {
        s += myarray[y][x];
        if (myflood[y][x] > s)
        {
            myflood[y][x] = s;
            visited++;
            flood_fill(x+1, y, s);
            flood_fill(x, y+1, s);
            flood_fill(x-1, y, s);
            flood_fill(x, y-1, s);
        }
    }
}


int main()
{
    std::vector<std::string> myinput = read_file("input15.txt");
    //fill_array(myinput);
    fill_array_times_five(myinput);

    // greedy pathfinding only going down and right:
    // find_path_looking_ahead(5);
    // print_track();

    // minima found:
    // <619 simple greedy
    // <594 with next 2
    // <552 with next 3
    // 490 with next 5
    // 478 with next 18
    // ... didnt work

    // flood fill:
    flood_fill(0, 0, 0);
    std::cout << "visited: " << visited << std::endl;
    std::cout << "total path risk: " << myflood[size-1][size-1] - myflood[0][0] << std::endl;
    // 472 is the answer
    // 2851 for 500x500 array - takes roughly 20 s to execute
}