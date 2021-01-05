#                      {
#                         "name": "",
#                         "authors": [],
#                         "args": [],
#                         "returns": [],
#                         "description": "",
#                         "keywords": [],
#                         "usage": ""}
#                       }


funcdict = {
  "modname": "mymod",
  "modvers": "0.1.6",
  "modroot": {
    "funcs": [
      {
        "name": "base_describe",
        "authors": ["John Omernik"],
        "args": [],
        "returns": [],
        "description": "A basic function that takes no arguments and returns nothing. Just prints a statement",
        "keywords": ["basic"],
        "usage": "mymod.base_describe()\n>>> This is a base level function to describe things"
     }
    ],
    "children": {
      "math_funcs": {
        "funcs": [
          {
            "name": "math_sum",
            "authors": ["John Omernik"],
            "args": [
              ["val1", "number", "req", "The first value to sum"],
              ["val2", "number", "req", "The second value to sum"]
            ],
            "returns": [
              ["number", "The added number of the types provided"]
            ],
            "description": "Adds two argument (val1 and val2) together",
            "keywords": ["sum", "add", "math", "basic"],
            "usage": "print(mymod.math_funcs.math_sum(5, 1))\n>>> 6"
          },
          {
            "name": "math_sub",
            "authors": ["John Omernik"],
            "args": [
              ["val1", "number", "req", "The value to subtract from"],
              ["val2", "number", "req", "The amount to subtract"]
            ],
            "returns": [
              ["number", "The subtracted number of the types provided"]
            ],
            "description": "Subtracts val2 from val1",
            "keywords": ["minus", "subtract", "math", "basic"],
            "usage": "print(mymod.math_funcs.math_sub(5, 1))\n>>> 4"
          },
          {
            "name": "math_mul",
            "authors": ["John Omernik"],
            "args": [
              ["val1", "number", "req", "The first value to multiply against"],
              ["val2", "number", "req", "The amount to multiply the first value"]
            ],
            "returns": [
              ["number", "The numbers multiplied in the type provided"]
            ],
            "description": "Multiplies val1 by val2",
            "keywords": ["multiply", "product", "math", "basic"],
            "usage": "print(mymod.math_funcs.math_mul(5, 6))\n>>> 30"
          },
          {
            "name": "math_div",
            "authors": ["John Omernik"],
            "args": [
              ["val1", "number", "req", "The dividend"],
              ["val2", "number", "req", "The divisor (No Zeros!)"]
            ],
            "returns": [
              ["number", "The quotient in the type provided"]
            ],
            "description": "Divides val1 by val2.  Returns the remainder. Makesure val2 isn't 0",
            "keywords": ["quotient", "division", "math", "basic"],
            "usage": "print(mymod.math_funcs.math_div(12, 6))\n>>> 2"
          }
        ],
        "children": {
          "adv_math": {
            "funcs": [
                       {
                         "name": "math_exp",
                         "authors": ["John Omernik"],
                         "args": [
                           ["val", "number", "req", "The value to be exponented. Could be a int or float"],
                           ["inttimes", "int", "req", "The number of times to exponent the val (must be int)"]
                         ],
                         "returns": [
                           ["number", "The type of number that was passed into the function"]
                         ],
                         "description": "Takes a number (val) and raises it to the (inttimes) power",
                         "keywords": ["exponent", "advanced"],
                         "usage": "print(mymod.math_funcs.adv_math.math_exp(5, 2))\n>>> 25"
                       }
                     ],
            "children": {}
          }
        }
      },
      "string_funcs": {
        "funcs": [
          {
            "name": "str_concat",
            "authors": ["John Omernik"],
            "args": [
                      ["val1", "str", "req", "The first value to concatentate"],
                      ["val2", "str", "req", "The second value to concatendate"],
                      ["sep", "str", "opt", "Optional seperator. If none is provided, will use a empty string ('')"]
                    ],
            "returns": [
                         ["str", "concatenated value"]
                       ],
            "description": "Takes two strs, val1 and vals and concatenates them together with an optional sep. If no sep is provided, '' (empty string) is used",
            "keywords": ["strings", "concat", "basic"],
            "usage": "v1 = 'Hello'\nv2 = 'Goodbye'\nprint(mymod.string_funcs.str_concat(v1, v2))\n\n>>> HelloGoodbye"
          },
          {
            "name": "str_split",
            "authors": ["John Omernik"],
            "args": [
                      ["splitstr", "str", "req", "The string to split"],
                      ["splitval", "str", "req", "The seperator to us to split on "]
                    ],
            "returns": [
                         ["list", "A list of values split"]
                       ],
            "description": "Takes a string, splitstr, and split it based on the value splitval. Returns a list of split items",
            "keywords": ["strings", "split", "basic"],
            "usage": "v1 = 'Hello,Goodbye'\nmylist = mymod.string_funcs.str_split(v1, ",")\n\nmylist>>> ['Hello', 'Goodbye']"
          }
        ],
        "children": {}
      }
    }
  }
}

