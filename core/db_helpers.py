def is_oracle(conn):
    return conn.__class__.__module__.startswith("cx_Oracle")

def param(style_count, oracle):
    if oracle:
        return ",".join([f":{i+1}" for i in range(style_count)])
    return ",".join(["%s"] * style_count)