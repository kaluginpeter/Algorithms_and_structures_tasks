/*
Background
Do you need a non-technical refresher on what a zip function is? Uncollapse
Task
Implement a zip function that accepts an arbitrary number of 1 or more (possibly different types of) containers and eagerly zips them into a std::vector of std::tuples.

Expectations
If the input container sizes are different, you must zip by the shortest (this is explained in the background section).

Your zipping mechanism should work with any container that meets the named requirement "Container" (Click the link to check out which operations a container allows you). This means you can't rely on random access, since not all containers are random access.

Since zip collects values at each index into a std::tuple, then if only a single argument is provided, zip should return a std::vector of one-element std::tuples.

For example:

zip(std::vector{ 1, 2, 3, 4 })
// returns
std::vector<std::tuple<int>>{ std::tuple{ 1 }, std::tuple{ 2 }, std::tuple{ 3 }, std::tuple{ 4 } }
Your returned vector should own its data. In other words, the returned std::tuple type should reflect the containers' "value type" (i.e., don't add CV qualifiers or references from your side). For example, zipping an int container with a char container should give back std::vector<std::tuple<int, char>>, and not std::vector<std::tuple<const int, char&>>.

Assumptions
The tests will never call your zip function with no arguments. One or more containers will always be provided. For the purposes of this kata, zipping 0 containers is not a defined operation.
You can be assured that all the supplied inputs meet the named requirement "Container". No need for safety checks.
Naturally, this means the tests will NOT involve classes that do not fully meet all of the requirements. Hence, std::forward_list and some container adapters like std::stack are out of scope.
Assuming and hardcoding a certain maximum arguments count in your solution makes it prone to invalidation by the tests at any time. Just use template packs as in the solution setup.
Although the following don't necessarily prove cheating, for my peace of mind, you will NOT be allowed to use:
The ranges/range-v3 library at large (sorry; can't be sure you're not bringing in views::zip_view)
The #define preprocessor directive
To make writing tests easier for myself, I decided not to involve containers like std::vector<bool> that return proxy types (This means that solutions that use the container's reference type (aka the element access type) as a (naive) substitute for the container's value type will not be penalized).
Example Usage
const std::multiset<int>       arg_1 = { 1, 2, 3, 4, 5, 6, 7, 8 };
const std::string              arg_2 = "abc";
const std::vector<std::string> arg_3 = { ":)", ":(", ":P", "xD", ":o", ":|" };

zip(arg_1, arg_2, arg_3)
==
std::vector<std::tuple<int, char, std::string>>{ { 1, 'a', ":)" }, { 2, 'b', ":(" }, { 3, 'c', ":P" } };
Note the return type, and how the number of returned tuples was limited by the shortest of the supplied containers.

Note
This isn't a performance kata at all, but your solution still shouldn't be too slow to compile. This is because the random tests are somewhat aggressive to make cheating infeasible. Once you add to that the extensive error logging I've set up, as well as the template-heavy code from your side, you'll likely notice that compilation times are slower than usual. This is expected. This is why I was careful and had to be stingier than I wanted to be with the magnitude and scope of tests. My solution finishes the full tests (comfortably below the timeout limit) at ~6-8s, as would most typical implementations. However, you shouldn't worry about your tests taking longer unless each run actually borders on timing out (>10s). If your tests time out (12s), you're probably being too indulgent with template instantiations.

MetaprogrammingFundamentalsLanguage FeaturesIteratorsRestricted
*/
// Solution
#include <tuple>
#include <vector>
#include <algorithm>
#include <iterator>

template <typename... Containers>
auto zip(const Containers&... containers)
{
    using tuple_type =
        std::tuple<typename Containers::value_type...>;

    const auto min_size =
        std::min({ containers.size()... });

    std::vector<tuple_type> result;
    result.reserve(min_size);

    auto iters = std::make_tuple(containers.begin()...);

    for (size_t i = 0; i < min_size; ++i)
    {
        result.emplace_back(
            std::apply(
                [](auto const&... it)
                {
                    return tuple_type(*it...);
                },
                iters
            )
        );

        std::apply(
            [](auto&... it)
            {
                ((++it), ...);
            },
            iters
        );
    }

    return result;
}