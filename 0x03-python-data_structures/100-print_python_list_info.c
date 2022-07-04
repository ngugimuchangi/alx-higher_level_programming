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

	/* check if pointer points to a list object */
	if (PyList_Check(temp))
	{
		/* print size of list object */
		printf("[*] Size of the Python List = %li\n", PyList_Size(temp));
		/**
		 * print allocated slots in list object
		 * note the casting of PyListObject pointer to PyObject pointer
		 * before accessing data
		 */
		printf("[*] Allocated = %li\n", ((PyListObject *)temp)->allocated);
		/* loop through the list object printing elements and their indices */
		for (i = 0; i < PyList_Size(temp); i++)
			printf("Element %li: %s\n", i, PY_TYPE(PyList_GetItem(temp, i))->tp_name);
	}
}
