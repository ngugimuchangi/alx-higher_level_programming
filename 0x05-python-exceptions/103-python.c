#include <stdio.h>
#include <Python.h>
/**
 * print_python_bytes - prints bytes of a string
 * @p: address of python object.
 *
 * Description: print size of bytes object,
 * the bytes object and its first 10 bytes in
 * hexadecimal.
 *
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	unsigned char size, c;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
	size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);
	for (c = 0; c < size; c++)
	{
		printf("%02hhx", bytes->ob_sval[c]);
		if (c == (size - 1))
		printf("\n");
		else
		printf(" ");
	}
}

/**
 * print_python_float - print info about PyFloat object
 * @p: address of PyFloat object
 *
 * Description: print float value of PyFloat object
 *
 * Return: nothing
 */
void print_python_float(PyObject *p)
{
	double i;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float"))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	i = ((PyFloatObject *) p)->ob_fval;
	printf("  value: %s\n", PyOS_double_to_string(
				i, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}

/**
 * print_python_list - print info about Python object
 * @p: address of python object
 *
 * Description: print size of list, allocated memory,
 * elements in the within the list and their type.
 * If element is a  object, print its basic info.
 *
 * Return: nothing
 */
void  print_python_list(PyObject *p)
{
	int size, i, alloc;
	PyVarObject *var = (PyVarObject *)p;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	size = var->ob_size;
	alloc = list->allocated;
	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!PyList_Check(list))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[i]);
		if (!strcmp(type, "float"))
			print_python_float(list->ob_item[i]);
	}
}
