#include <vector>
#include <array>
#include <iostream>
#include <cstdlib>

const static int n = 9;     // no of data points

float s_x_lev2 (int dim1, int dim2, int i, int j, std::array<float, n> X1_list, std::array<float, n> X2_list)
{
    std::array<float, n> dim1_list = {0};
    std::array<float, n> dim2_list = {0};

    if(dim1 == 1)
    {
        dim1_list = X1_list;
    } else
    {
        dim1_list = X2_list;
    }

    if(dim2 == 1)
    {
        dim2_list = X1_list;
    } else
    {
        dim2_list = X2_list;
    }

    float tot = 0;
    float integ = 0;
    for(int m = i; m < j; m++)
    {
        integ = (dim2_list.at(m+1) - dim2_list.at(m))*((dim1_list.at(m) - dim1_list.at(i)) + 0.5*(dim1_list.at(m+1) - dim1_list.at(m)));
        tot = tot + integ;
    }
    return tot;
}

float s_x_lev3 (int dim1, int dim2, int dim3, int i, int j, std::array<float, n> X1_list, std::array<float, n> X2_list)
{
    std::array<float, n> dim1_list = {0};
    std::array<float, n> dim2_list = {0};
    std::array<float, n> dim3_list = {0};

    if(dim1 == 1)
    {
        dim1_list = X1_list;
    } else
    {
        dim1_list = X2_list;
    }

    if(dim2 == 1)
    {
        dim2_list = X1_list;
    } else
    {
        dim2_list = X2_list;
    }

    if(dim3 == 1)
    {
        dim3_list = X1_list;
    } else
    {
        dim3_list = X2_list;
    }

    float tot = 0;
    float integ = 0;
    for(int m = i; m < j; m++)
    {
        integ = (dim3_list.at(m+1) - dim3_list.at(m))*(s_x_lev2(dim1, dim2, i, m, X1_list, X2_list)
                                                       + (dim1_list.at(m) - dim1_list.at(i))*(dim2_list.at(m+1) - dim2_list.at(m))/2.0
                                                       + (dim1_list.at(m+1) - dim1_list.at(m))*(dim2_list.at(m+1) - dim2_list.at(m))/6.0
                                                       );
        tot = tot + integ;
    }
    return tot;
}

int main()
{
    std::array<float, n> X1 = {1, 0.707, 0, -0.707, -1, -0.707, 0, 0.707, 1};
    std::array<float, n> X2 = {0, 0.707, 1, 0.707, 0, -0.707, -1, -0.707, 0};


    int t_i = 0;
    int t_j = 8;
    std::cout << "Enter i of t_i (<t_j) : ";
    std::cin >> t_i;
    std::cout << "Enter j of t_j (>t_i) : ";
    std::cin >> t_j;
    std::cout << std::endl;

    for(int k = 1; k <= 2; k++)
    {
        for(int l = 1; l <= 2; l++)
        {
            std::cout << "S(X)_" << k << "," << l << " = " << s_x_lev2(k, l, t_i, t_j, X1, X2) << std::endl;
        }
    }

    std::cout << std::endl;

    for(int k = 1; k <= 2; k++)
    {
        for(int l = 1; l <= 2; l++)
        {
            for(int p = 1; p <= 2; p++)
            {
                std::cout << "S(X)_" << k << "," << l << "," << p << " = " << s_x_lev3(k, l, p, t_i, t_j, X1, X2) << std::endl;
            }
        }
    }

    return 0;
}
