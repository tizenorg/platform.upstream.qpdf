%define _unpackaged_files_terminate_build 0

Summary: Command-line tools and library for transforming PDF files
Name: qpdf
Version: 3.0.2
Release: 2
License: Artistic
Group: System Environment/Libraries
URL: http://qpdf.sourceforge.net/
Source: %{name}-%{version}.tar.gz
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libpcre)

%description
QPDF is a program that does structural, content-preserving
transformations on PDF files.  It could have been called something
like pdf-to-pdf.  It also provides many useful capabilities to
developers of PDF-producing software or for people who just want to
look at the innards of a PDF file to learn more about how they work.

QPDF offers many capabilities such as linearization (web
optimization), encrypt, and decription of PDF files.  Note that QPDF
does not have the capability to create PDF files from scratch; it is
only used to create PDF files with special characteristics starting
from other PDF files or to inspect or extract information from
existing PDF files.

%package devel
Summary: Development files for qpdf PDF manipulation library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release} zlib-devel libpcre-devel

%description devel
The qpdf-devel package contains header files and libraries necessary
for developing programs using the qpdf library.

%package static
Summary: Static QPDF library
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}

%description static
The qpdf-static package contains the static qpdf library.

%prep
%setup -q

%build
./autogen.sh
%configure --without-docdir
#    --docdir='${datarootdir}'/doc/%{name}-%{version}

make %{?_smp_mflags}
make check

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
# %doc below clobbers our docdir, so we have to copy it to a safe
# place so we can install it using %doc.  We should still set docdir
# properly when configuring so that it gets substituted properly by
# autoconf.
#cp -a $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version} install-docs
#mkdir -p install-examples/examples
#cp -p examples/*.cc examples/*.c install-examples/examples
# Red Hat doesn't ship .la files.
#rm -f $RPM_BUILD_ROOT%{_libdir}/libqpdf.la

mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{buildsubdir}/Artistic-2.0 %{buildroot}/usr/share/license/%{name}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%manifest qpdf.manifest
%defattr(-,root,root)
#README TODO Artistic-2.0 install-docs/*
/usr/share/license/%{name}
%exclude %{_bindir}/*
%{_libdir}/libqpdf*.so.*
%exclude %{_mandir}/man1/*

%files devel
%defattr(-,root,root)
#install-examples/examples
%{_includedir}/*
%{_libdir}/libqpdf*.so
%{_libdir}/pkgconfig

%files static
%defattr(-,root,root)
%{_libdir}/libqpdf*.a

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Apr 28 2008 Jay Berkenbilt <ejb@ql.org> - 2.0-1
- Initial packaging
