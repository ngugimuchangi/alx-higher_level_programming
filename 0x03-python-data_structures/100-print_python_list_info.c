#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints info on Python lists
 * @p: pointer to python object
 *
 * Description: prints size of list, allocated fields and
 * the elements within list and their types.
 *
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	long int i;
	PyObject *element;

	/* Print size of list object */
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	/**
	 * print allocated slots in list object
	 * note the casting of PyListObject pointer to PyObject pointer
	 * before accessing data
	 */
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	/* loop through the list object printing elements and their indices */
	for (i = 0; i < PyList_Size(p); i++)
	{
		element = PyList_Get_Item(p, i);
		printf("Element %ld: %s\n", i, PY_TYPE(element)->tp_name);
	}
}
