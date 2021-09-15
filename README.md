<h1 align="center">
  django-account
</h1>

<p align="center">
  <a href="#installation">Installation</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

<p align="center">Custom, simple Django User model with only email and name fields</p>

## Installation

1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install numiner.

```bash
$ pip install account
```

2. Register the app to your settings

```python
INSTALLED_APPS = (
    ...
    'account',
)
```

3. Since it's a custom User model Django needs to know the path of the model

```bash
AUTH_USER_MODEL = 'account.User'
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT License](https://choosealicense.com/licenses/mit/)
