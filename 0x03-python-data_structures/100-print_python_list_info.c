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
	long int i, size, alloc;
	PyObject *element;

	/* Print size of list object */
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	/**
	 * print allocated slots in list object
	 * note the casting of PyListObject pointer to PyObject pointer
	 * before accessing data
	 */
	alloc =  ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %ld\n", alloc);
	/* loop through the list object printing elements and their indices */
	for (i = 0; i < size; i++)
	{
		element = PyList_Get_Item(p, i);
		printf("Element %ld: %s\n", i, PY_TYPE(element)->tp_name);
	}
}
