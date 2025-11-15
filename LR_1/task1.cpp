#include <list>
#include <stack>
using namespace std;

list<string> li {"x", "1", "y", "2", "z", "3"};  // список (специализированный контейнер)

stack<string> stack;  // стек
stack.push("x");  // push - добавление в стек
stack.push("y");
stack.push("z");
