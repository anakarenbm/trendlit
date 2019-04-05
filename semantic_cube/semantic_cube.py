from semantic_cube.semantic_cube_helper import token_to_code, type_to_code

type_int = type_to_code.get("int")
type_double = type_to_code.get("double")
type_bool = type_to_code.get("bool")
type_error = type_to_code.get("error")
type_none = -1


class Cube:
    def __init__(self):
        self.cube = {
            # INT with all other primitive data types.
            (type_int, type_int, token_to_code.get("+")): type_int,
            (type_int, type_int, token_to_code.get("-")): type_int,
            (type_int, type_int, token_to_code.get("*")): type_int,
            (type_int, type_int, token_to_code.get("/")): type_double,
            (type_int, type_int, token_to_code.get("<")): type_bool,
            (type_int, type_int, token_to_code.get(">")): type_bool,
            (type_int, type_int, token_to_code.get("<=")): type_bool,
            (type_int, type_int, token_to_code.get(">=")): type_bool,
            (type_int, type_int, token_to_code.get("is")): type_bool,
            (type_int, type_int, token_to_code.get("not")): type_bool,
            (type_int, type_int, token_to_code.get("and")): type_error,
            (type_int, type_int, token_to_code.get("or")): type_error,
            (type_int, type_int, token_to_code.get("=")): type_int,
            (type_none, type_int, token_to_code.get("UMINUS")): type_int,
            (type_int, type_double, token_to_code.get("+")): type_double,
            (type_int, type_double, token_to_code.get("-")): type_double,
            (type_int, type_double, token_to_code.get("*")): type_double,
            (type_int, type_double, token_to_code.get("/")): type_double,
            (type_int, type_double, token_to_code.get("%")): type_error,
            (type_int, type_double, token_to_code.get("<")): type_bool,
            (type_int, type_double, token_to_code.get(">")): type_bool,
            (type_int, type_double, token_to_code.get("<=")): type_bool,
            (type_int, type_double, token_to_code.get(">=")): type_bool,
            (type_int, type_double, token_to_code.get("is")): type_bool,
            (type_int, type_double, token_to_code.get("not")): type_bool,
            (type_int, type_double, token_to_code.get("and")): type_error,
            (type_int, type_double, token_to_code.get("or")): type_error,
            (type_int, type_double, token_to_code.get("=")): type_int,
            (type_int, type_bool, token_to_code.get("+")): type_error,
            (type_int, type_bool, token_to_code.get("-")): type_error,
            (type_int, type_bool, token_to_code.get("*")): type_error,
            (type_int, type_bool, token_to_code.get("/")): type_error,
            (type_int, type_bool, token_to_code.get("%")): type_error,
            (type_int, type_bool, token_to_code.get("<")): type_error,
            (type_int, type_bool, token_to_code.get(">")): type_error,
            (type_int, type_bool, token_to_code.get("<=")): type_error,
            (type_int, type_bool, token_to_code.get(">=")): type_error,
            (type_int, type_bool, token_to_code.get("is")): type_error,
            (type_int, type_bool, token_to_code.get("not")): type_error,
            (type_int, type_bool, token_to_code.get("and")): type_error,
            (type_int, type_bool, token_to_code.get("or")): type_error,
            (type_int, type_bool, token_to_code.get("=")): type_error,
            # DOUBLE with all other primitive data types.
            (type_double, type_double, token_to_code.get("+")): type_double,
            (type_double, type_double, token_to_code.get("-")): type_double,
            (type_double, type_double, token_to_code.get("*")): type_double,
            (type_double, type_double, token_to_code.get("/")): type_double,
            (type_double, type_double, token_to_code.get("%")): type_error,
            (type_double, type_double, token_to_code.get("<")): type_bool,
            (type_double, type_double, token_to_code.get(">")): type_bool,
            (type_double, type_double, token_to_code.get("<=")): type_bool,
            (type_double, type_double, token_to_code.get(">=")): type_bool,
            (type_double, type_double, token_to_code.get("is")): type_bool,
            (type_double, type_double, token_to_code.get("not")): type_bool,
            (type_double, type_double, token_to_code.get("and")): type_error,
            (type_double, type_double, token_to_code.get("or")): type_error,
            (type_double, type_double, token_to_code.get("=")): type_double,
            (type_none, type_double, token_to_code.get("UMINUS")): type_double,
            (type_double, type_int, token_to_code.get("+")): type_double,
            (type_double, type_int, token_to_code.get("-")): type_double,
            (type_double, type_int, token_to_code.get("*")): type_double,
            (type_double, type_int, token_to_code.get("/")): type_double,
            (type_double, type_int, token_to_code.get("%")): type_error,
            (type_double, type_int, token_to_code.get("<")): type_bool,
            (type_double, type_int, token_to_code.get(">")): type_bool,
            (type_double, type_int, token_to_code.get("<=")): type_bool,
            (type_double, type_int, token_to_code.get(">=")): type_bool,
            (type_double, type_int, token_to_code.get("is")): type_bool,
            (type_double, type_int, token_to_code.get("not")): type_bool,
            (type_double, type_int, token_to_code.get("and")): type_error,
            (type_double, type_int, token_to_code.get("or")): type_error,
            (type_double, type_int, token_to_code.get("=")): type_double,
            (type_double, type_bool, token_to_code.get("+")): type_error,
            (type_double, type_bool, token_to_code.get("-")): type_error,
            (type_double, type_bool, token_to_code.get("*")): type_error,
            (type_double, type_bool, token_to_code.get("/")): type_error,
            (type_double, type_bool, token_to_code.get("%")): type_error,
            (type_double, type_bool, token_to_code.get("<")): type_error,
            (type_double, type_bool, token_to_code.get(">")): type_error,
            (type_double, type_bool, token_to_code.get("<=")): type_error,
            (type_double, type_bool, token_to_code.get(">=")): type_error,
            (type_double, type_bool, token_to_code.get("is")): type_error,
            (type_double, type_bool, token_to_code.get("not")): type_error,
            (type_double, type_bool, token_to_code.get("and")): type_error,
            (type_double, type_bool, token_to_code.get("or")): type_error,
            (type_double, type_bool, token_to_code.get("=")): type_error,
            # BOOL with all other data types
            (type_bool, type_bool, token_to_code.get("+")): type_bool,
            (type_bool, type_bool, token_to_code.get("-")): type_error,
            (type_bool, type_bool, token_to_code.get("*")): type_bool,
            (type_bool, type_bool, token_to_code.get("/")): type_error,
            (type_bool, type_bool, token_to_code.get("%")): type_error,
            (type_bool, type_bool, token_to_code.get("<")): type_error,
            (type_bool, type_bool, token_to_code.get(">")): type_error,
            (type_bool, type_bool, token_to_code.get("<=")): type_error,
            (type_bool, type_bool, token_to_code.get(">=")): type_error,
            (type_bool, type_bool, token_to_code.get("is")): type_bool,
            (type_bool, type_bool, token_to_code.get("not")): type_bool,
            (type_bool, type_bool, token_to_code.get("and")): type_bool,
            (type_bool, type_bool, token_to_code.get("or")): type_bool,
            (type_bool, type_bool, token_to_code.get("=")): type_bool,
            (type_none, type_bool, token_to_code.get("UMINUS")): type_error,
            (type_bool, type_int, token_to_code.get("+")): type_error,
            (type_bool, type_int, token_to_code.get("-")): type_error,
            (type_bool, type_int, token_to_code.get("*")): type_error,
            (type_bool, type_int, token_to_code.get("/")): type_error,
            (type_bool, type_int, token_to_code.get("%")): type_error,
            (type_bool, type_int, token_to_code.get("<")): type_error,
            (type_bool, type_int, token_to_code.get(">")): type_error,
            (type_bool, type_int, token_to_code.get("<=")): type_error,
            (type_bool, type_int, token_to_code.get(">=")): type_error,
            (type_bool, type_int, token_to_code.get("is")): type_error,
            (type_bool, type_int, token_to_code.get("not")): type_error,
            (type_bool, type_int, token_to_code.get("and")): type_error,
            (type_bool, type_int, token_to_code.get("or")): type_error,
            (type_bool, type_int, token_to_code.get("=")): type_error,
            (type_bool, type_double, token_to_code.get("+")): type_error,
            (type_bool, type_double, token_to_code.get("-")): type_error,
            (type_bool, type_double, token_to_code.get("*")): type_error,
            (type_bool, type_double, token_to_code.get("/")): type_error,
            (type_bool, type_double, token_to_code.get("%")): type_error,
            (type_bool, type_double, token_to_code.get("<")): type_error,
            (type_bool, type_double, token_to_code.get(">")): type_error,
            (type_bool, type_double, token_to_code.get("<=")): type_error,
            (type_bool, type_double, token_to_code.get(">=")): type_error,
            (type_bool, type_double, token_to_code.get("is")): type_error,
            (type_bool, type_double, token_to_code.get("not")): type_error,
            (type_bool, type_double, token_to_code.get("and")): type_error,
            (type_bool, type_double, token_to_code.get("or")): type_error,
            (type_bool, type_double, token_to_code.get("=")): type_error,
        }

    def is_in_cube(self, operType1, operType2, op):
        if (operType1, operType2, op) not in self.cube:
            return False
        else:
            return True