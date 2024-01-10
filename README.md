# VehiclesAPI

An API for register and consult vehicles.

## Setup API

Create and active your virtual environment using the command bellow:

```bash
python3 -m venv .venv
```

```bash
python3 source .venv/bin/activate
```

if you are using windows, maybe the alias for your interpreter is different, try trade `python3` for `python` only.

## Making migrations

Create your `db.sqlite3` and all tables necessary with one commmand bellow:

```bash
python3 manage.py migrate
```

## Runserver

Run your api for listen by default in `localhost:8000`.

```bash
python3 manage.py runserver
```

## API Reference

### List all vehicles:

```bash
GET http://localhost:8000/api/vehicles/
```

### Create a vehicle:

```bash
POST http://localhost:8000/api/vehicles/
```

<table>
  <thead>
    <tr>
      <td>Parameter</td>
      <td>Type</td>
      <td>Description</td>
    </tr>
  </thead>
  <tbbody>
    <tr>
      <td>name</td>
      <td>string</td>
      <td>Required</td>
    </tr>
    <tr>
      <td>model</td>
      <td>string</td>
      <td>Required</td>
    </tr>
    <tr>
      <td>price</td>
      <td>float</td>
      <td>Required</td>
    </tr>
    <tr>
      <td>speed</td>
      <td>int</td>
      <td>Required</td>
    </tr>
    <tr>
      <td>passengers</td>
      <td>int</td>
      <td>Required</td>
    </tr>
    <tr>
      <td>year</td>
      <td>int</td>
      <td>Required</td>
    </tr>
  </tbody>
</table>

### List a specific vehicle

```bash
GET http://localhost:8000/api/vehicles/${id}/
```

### Update vehicle

```bash
PUT http://localhost:8000/api/vehicles/${id}/
```

<table>
  <thead>
    <tr>
      <td>Parameter</td>
      <td>Type</td>
      <td>Description</td>
    </tr>
  </thead>
  <tbbody>
    <tr>
      <td>name</td>
      <td>string</td>
      <td>Required</td>
    </tr>
    <tr>
      <td>model</td>
      <td>string</td>
      <td>Required</td>
    </tr>
    <tr>
      <td>price</td>
      <td>float</td>
      <td>Required</td>
    </tr>
    <tr>
      <td>speed</td>
      <td>int</td>
      <td>Required</td>
    </tr>
    <tr>
      <td>passengers</td>
      <td>int</td>
      <td>Required</td>
    </tr>
    <tr>
      <td>year</td>
      <td>int</td>
      <td>Required</td>
    </tr>
  </tbody>
</table>

### Delete vehicle

```bash
DELETE http://localhost:8000/api/vehicles/${id}/
```

> Keep in mind to change `${id}` for correspondent object what you want to play.