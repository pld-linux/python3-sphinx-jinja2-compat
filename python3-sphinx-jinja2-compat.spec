Summary:	Patches Jinja2 v3 to restore compatibility with earlier Sphinx versions
Name:		python3-sphinx-jinja2-compat
Version:	0.3.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-jinja2-compat/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx_jinja2_compat/sphinx_jinja2_compat-%{version}.tar.gz
# Source0-md5:	7834135e0a6eb6b3e8db7b8ef38cca10
Patch0:		deps.patch
URL:		https://github.com/sphinx-toolbox/sphinx-jinja2-compat
BuildRequires:	python3 >= 1:3.6
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-whey
BuildRequires:	python3-whey-pth
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Patches Jinja2 v3 to restore compatibility with earlier Sphinx
versions.

%prep
%setup -q -n sphinx_jinja2_compat-%{version}
%patch -P0 -p1

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/_sphinx_jinja2_compat.pth
%dir %{py3_sitescriptdir}/sphinx_jinja2_compat
%{py3_sitescriptdir}/sphinx_jinja2_compat/*.py
%{py3_sitescriptdir}/sphinx_jinja2_compat/__pycache__
%{py3_sitescriptdir}/sphinx_jinja2_compat-%{version}.dist-info
