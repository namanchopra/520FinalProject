# Patient Tracker App

**This is an app for patients and doctors to keep track of medical records, and prescriptions.**

The patient may have multiple doctors, prescriptions, and medical records that they want to view.

The doctor may have multiple patients, prescriptions, and medical records that they see, create, and update.

A system admin can remove patients and doctors, and can view system logs.

Patients may or may not have insurance

Doctors might be able to accept some insurance providers, but not others.

Users are able to search for doctors by their name, specialization and 

### Build & Run Patient Tracker
The app is designed to run with Python 3 and MySQL
to use mysql-connector, you need to install it:

``pip install mysql-connector-python``

The app also uses Tkinter, which is a front-end library which comes prepackaged with Python, but if you have uninstalled it for whatever reason, it can be installed with ``pip install tk`` and optionally with the flags ``--force-reinstall --upgrade``

Run the application from the main application directory with ``python patientTracker.py`` or ``python3 patientTracker.py``

### Data & Privacy Policy

User data is stored securely in our database. Your information is *never* shared with or seen by anyone whom you have not permitted to see it. While we must store your email, password, name, age, insurance provider, prescriptions, and medical records, our system administrators can not view any patient information other than name and email so as to not breach doctor-patient confidentiality. Only your doctor(s) may view your name, age, insurance provider, prescriptions, and medical records.