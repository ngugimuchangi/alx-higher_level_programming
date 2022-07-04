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
	long int i
	PyObject *temp = p;

	if (PyList_Check(temp))
	{
		printf("[*] Size of the Python List = %li\n", PyList_Size(temp));
		printf("[*] Allocated = %li\n", temp->allocated)
		for (i = 0; i < PyList_Size(temp); i++)
			printf("Element %li: %s\n", i, PY_TYPE(PyList_GetItem(temp, i))->tp_name);
	}
}
