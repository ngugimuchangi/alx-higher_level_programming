#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 * print_python_string - prints Python strings
 * @p: Python Object
 * Return: void
 */
void print_python_string(PyObject *p)
{
	PyObject *str, *repr;
	char *text;

	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	repr = PyObject_Repr(p);
	str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
	text = PyBytes_AsString(str);
	printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
	printf("  str = %s\n", text);
}
