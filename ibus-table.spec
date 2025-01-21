#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : ibus-table
Version  : 1.17.10
Release  : 13
URL      : https://github.com/mike-fabian/ibus-table/releases/download/1.17.10/ibus-table-1.17.10.tar.gz
Source0  : https://github.com/mike-fabian/ibus-table/releases/download/1.17.10/ibus-table-1.17.10.tar.gz
Summary  : The Table engine for IBus platform
Group    : Development/Tools
License  : LGPL-2.0+ LGPL-2.1
Requires: ibus-table-bin = %{version}-%{release}
Requires: ibus-table-data = %{version}-%{release}
Requires: ibus-table-libexec = %{version}-%{release}
Requires: ibus-table-license = %{version}-%{release}
Requires: ibus-table-locales = %{version}-%{release}
Requires: ibus-table-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gettext
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(ibus-1.0)
BuildRequires : pygobject-python3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The package contains general Table engine for IBus platform.

%package bin
Summary: bin components for the ibus-table package.
Group: Binaries
Requires: ibus-table-data = %{version}-%{release}
Requires: ibus-table-libexec = %{version}-%{release}
Requires: ibus-table-license = %{version}-%{release}

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
Requires: ibus-table-bin = %{version}-%{release}
Requires: ibus-table-data = %{version}-%{release}
Provides: ibus-table-devel = %{version}-%{release}
Requires: ibus-table = %{version}-%{release}

%description dev
dev components for the ibus-table package.


%package libexec
Summary: libexec components for the ibus-table package.
Group: Default
Requires: ibus-table-license = %{version}-%{release}

%description libexec
libexec components for the ibus-table package.


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


%package man
Summary: man components for the ibus-table package.
Group: Default

%description man
man components for the ibus-table package.


%prep
%setup -q -n ibus-table-1.17.10
cd %{_builddir}/ibus-table-1.17.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1737496653
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1737496653
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ibus-table
cp %{_builddir}/ibus-table-%{version}/COPYING %{buildroot}/usr/share/package-licenses/ibus-table/caeb68c46fa36651acf592771d09de7937926bb3 || :
export GOAMD64=v2
GOAMD64=v2
%make_install
%find_lang ibus-table

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ibus-table-createdb

%files data
%defattr(-,root,root,-)
/usr/share/applications/ibus-setup-table.desktop
/usr/share/glib-2.0/schemas/org.freedesktop.ibus.engine.table.gschema.xml
/usr/share/ibus-table/data/coin9.wav
/usr/share/ibus-table/data/phrase.txt.bz2
/usr/share/ibus-table/data/pinyin_table.txt.bz2
/usr/share/ibus-table/engine/chinese_variants.py
/usr/share/ibus-table/engine/factory.py
/usr/share/ibus-table/engine/ibus_table_location.py
/usr/share/ibus-table/engine/it_active_window.py
/usr/share/ibus-table/engine/it_sound.py
/usr/share/ibus-table/engine/it_util.py
/usr/share/ibus-table/engine/main.py
/usr/share/ibus-table/engine/tabcreatedb.py
/usr/share/ibus-table/engine/table.py
/usr/share/ibus-table/engine/tabsqlitedb.py
/usr/share/ibus-table/engine/version.py
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
/usr/share/ibus-table/setup/i18n.py
/usr/share/ibus-table/setup/main.py
/usr/share/ibus-table/setup/version.py
/usr/share/ibus-table/tables/template.txt
/usr/share/ibus/component/table.xml
/usr/share/icons/hicolor/128x128/apps/ibus-table.png
/usr/share/icons/hicolor/16x16/apps/ibus-table.png
/usr/share/icons/hicolor/22x22/apps/ibus-table.png
/usr/share/icons/hicolor/256x256/apps/ibus-table.png
/usr/share/icons/hicolor/32x32/apps/ibus-table.png
/usr/share/icons/hicolor/48x48/apps/ibus-table.png
/usr/share/icons/hicolor/64x64/apps/ibus-table.png
/usr/share/icons/hicolor/scalable/apps/ibus-table.svg
/usr/share/metainfo/org.freedesktop.ibus.engine.table.metainfo.xml

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/ibus-table.pc

%files libexec
%defattr(-,root,root,-)
/usr/libexec/ibus-engine-table
/usr/libexec/ibus-setup-table

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ibus-table/caeb68c46fa36651acf592771d09de7937926bb3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ibus-table-createdb.1

%files locales -f ibus-table.lang
%defattr(-,root,root,-)

