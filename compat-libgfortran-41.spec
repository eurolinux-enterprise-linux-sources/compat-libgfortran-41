%define DATE 20071221
%define _unpackaged_files_terminate_build 0
Summary: Compatibility Fortran 95 runtime library version 4.1.2
Name: compat-libgfortran-41
Version: 4.1.2
Release: 44%{?dist}
# libgfortran has an exception which allows
# linking it into any kind of programs or shared libraries without
# restrictions.
License: GPLv2+ with exceptions
Group: System Environment/Libraries
Source0: libgfortran-%{version}-%{DATE}.tar.bz2
URL: http://gcc.gnu.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gcc-gfortran >= 4.1.2, gettext, bison, flex, texinfo
Patch1: libgfortran41-gthr.patch

%description
This package includes a Fortran 95 runtime library for compatibility
with GCC 4.1.x-RH compiled Fortran applications.

%prep
%setup -q -n libgfortran-%{version}-%{DATE}
%patch1 -p0 -b .gthr~

%build
mkdir obj
cd obj
CFLAGS="$RPM_OPT_FLAGS" FCFLAGS="$RPM_OPT_FLAGS" ../libgfortran/configure --prefix=%{_prefix} --disable-multilib
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd obj
mkdir -p $RPM_BUILD_ROOT%{_libdir}
install -m 755 .libs/libgfortran.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}/
ln -sf libgfortran.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}/libgfortran.so.1

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libgfortran.so.1*

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 4.1.2-44
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 4.1.2-43
- Mass rebuild 2013-12-27

* Wed Aug 28 2013 Jakub Jelinek <jakub@redhat.com 4.1.2-42
- add %%{?dist} to Release (#874994)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 21 2007 Jakub Jelinek  <jakub@redhat.com> 4.1.2-36
- new compat library
