Name:           qpdf
Version:        3.0.2
Release:        0
License:        Artistic-2.0
Summary:        Command-line tools and library for transforming PDF files
Url:            http://qpdf.sourceforge.net/
Group:          System/Libraries
Source:         %{name}-%{version}.tar.gz
Source1:        %{name}.manifest
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(zlib)

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
Summary:        Development files for qpdf PDF manipulation library
Group:          Development/System
Requires:       %{name} = %{version}
Requires:       pkgconfig(libpcre)
Requires:       pkgconfig(zlib)

%description devel
The qpdf-devel package contains header files and libraries necessary
for developing programs using the qpdf library.


%prep
%setup -q
cp %{SOURCE1} .

%build
./autogen.sh
%configure --without-docdir

make %{?_smp_mflags}

%check
make check

%install
%make_install
rm -rf %{buildroot}/%{_datadir}/doc/qpdf
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%docs_package

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license Artistic-2.0 
%exclude %{_bindir}/*
%{_libdir}/libqpdf*.so.*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libqpdf*.so
%{_libdir}/pkgconfig/*.pc


%changelog
