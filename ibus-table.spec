#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ibus-table
Version  : 1.5.0
Release  : 2
URL      : http://mfabian.fedorapeople.org/ibus-table/ibus-table-1.5.0.tar.gz
Source0  : http://mfabian.fedorapeople.org/ibus-table/ibus-table-1.5.0.tar.gz
Summary  : The Table engine for IBus platform
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: ibus-table-bin
Requires: ibus-table-license
Requires: ibus-table-data
Requires: ibus-table-locales
BuildRequires : gettext
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(ibus-1.0)

%description
The package contains general Table engine for IBus platform.

%package bin
Summary: bin components for the ibus-table package.
Group: Binaries
Requires: ibus-table-data
Requires: ibus-table-license

%description bin
bin components for the ibus-table package.


%package data
Summary: data components for the ibus-table package.
Group: Data

%description data
data components for the ibus-table package.


%package dev
Summary: dev components for the ibus-table package.
Group: Development
Requires: ibus-table-bin
Requires: ibus-table-data
Provides: ibus-table-devel

%description dev
dev components for the ibus-table package.


%package license
Summary: license components for the ibus-table package.
Group: Default

%description license
license components for the ibus-table package.


%package locales
Summary: locales components for the ibus-table package.
Group: Default

%description locales
locales components for the ibus-table package.


%prep
%setup -q -n ibus-table-1.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536448190
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1536448190
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/ibus-table
cp COPYING %{buildroot}/usr/share/doc/ibus-table/COPYING
%make_install
%find_lang ibus-table

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ibus-table-createdb
/usr/libexec/ibus-engine-table

%files data
%defattr(-,root,root,-)
/usr/share/ibus-table/data/pinyin_table.txt.bz2
/usr/share/ibus-table/engine/factory.py
/usr/share/ibus-table/engine/main.py
/usr/share/ibus-table/engine/tabcreatedb.py
/usr/share/ibus-table/engine/tabdict.py
/usr/share/ibus-table/engine/table.py
/usr/share/ibus-table/engine/tabsqlitedb.py
/usr/share/ibus-table/icons/acommit.svg
/usr/share/ibus-table/icons/cb-mode.svg
/usr/share/ibus-table/icons/chinese.svg
/usr/share/ibus-table/icons/english.svg
/usr/share/ibus-table/icons/full-letter.svg
/usr/share/ibus-table/icons/full-punct.svg
/usr/share/ibus-table/icons/half-letter.svg
/usr/share/ibus-table/icons/half-punct.svg
/usr/share/ibus-table/icons/ibus-table.svg
/usr/share/ibus-table/icons/ncommit.svg
/usr/share/ibus-table/icons/onechar.svg
/usr/share/ibus-table/icons/phrase.svg
/usr/share/ibus-table/icons/py-mode.svg
/usr/share/ibus-table/icons/sc-mode.svg
/usr/share/ibus-table/icons/scb-mode.svg
/usr/share/ibus-table/icons/tab-mode.svg
/usr/share/ibus-table/icons/tc-mode.svg
/usr/share/ibus-table/icons/tcb-mode.svg
/usr/share/ibus-table/tables/template.txt
/usr/share/ibus/component/table.xml

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/ibus-table.pc

%files license
%defattr(-,root,root,-)
/usr/share/doc/ibus-table/COPYING

%files locales -f ibus-table.lang
%defattr(-,root,root,-)

