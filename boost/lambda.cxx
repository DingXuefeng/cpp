#include <boost/lambda/lambda.hpp>
#include <iostream>
#include <iterator>
#include <algorithm>
#include <vector>

int main()
{
    using namespace boost::lambda;
    typedef std::istream_iterator<int> in;
    std::vector<int> a;
    a.push_back(3);
    a.push_back(4);
    a.push_back(3);
    a.push_back(31);
    std::for_each(a.begin(),a.end(),std::cout<<_1<<" ");

//    std::for_each(
//        in(std::cin), in(), std::cout << (_1 * 3) << " " );
}
