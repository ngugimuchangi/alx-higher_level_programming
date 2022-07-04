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
	PyListObject *list;
	Py_ssize_t l_size, i;
	PyObject *obj;
	struct _typeobject *el_type;

	if (strcmp(p->ob_type->tp_name, "list") == 0)
	{
		list = (PyListObject *)p;
		l_size = list->ob_base.ob_size;
		printf("[*] Size of the Python List = %ld\n", l_size);
		printf("[*] Allocated = %ld\n", list->allocated);
		for (i = 0; i < l_size; i++)
		{
			obj = list->ob_item[i];
			el_type = obj->ob_type;
			printf("Element %ld: %s\n", i, el_type->tp_name);
		}
	}
}
