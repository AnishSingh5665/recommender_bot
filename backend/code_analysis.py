import ast

def analyze_code(code_str):
    try:
        tree = ast.parse(code_str)
        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        return {
            "functions_found": functions,
            "num_lines": len(code_str.splitlines())
        }
    except Exception as e:
        return {"error": str(e)}
