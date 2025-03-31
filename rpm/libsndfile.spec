Name:       libsndfile
Summary:    Library for reading and writing sound files
Version:    1.2.2
Release:    1
License:    LGPLv2+
URL:        https://github.com/sailfishos/libsndfile
Source0:    libsndfile-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  cmake
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(opus)

%description
libsndfile is a C library for reading and writing sound files such as
AIFF, AU, WAV, and others through one standard interface. It can
currently read/write 8, 16, 24 and 32-bit PCM files as well as 32 and
64-bit floating point WAV files and a number of compressed formats. It
compiles and runs on *nix, MacOS, and Win32.

%package devel
Summary:    Development files for libsndfile
Requires:   %{name} = %{version}-%{release}

%description devel
libsndfile is a C library for reading and writing sound files such as
AIFF, AU, WAV, and others through one standard interface.
This package contains files needed to develop with libsndfile.

%package utils
Summary:    Command Line Utilities for libsndfile
Requires:   %{name} = %{version}-%{release}

%description utils
libsndfile is a C library for reading and writing sound files such as
AIFF, AU, WAV, and others through one standard interface.
This package contains command line utilities for libsndfile.

%package doc
Summary:    Documentation for %{name}
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description doc
Man pages for %{name}.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%cmake -DBUILD_SHARED_LIBS=ON -DBUILD_EXAMPLES=OFF

%make_build

%install
%make_install

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
mv %{buildroot}%{_docdir}/%{name} \
   %{buildroot}%{_docdir}/%{name}-%{version}/html

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/%{name}.so.*

%files utils
%{_bindir}/sndfile-*
%{_mandir}/man1/sndfile-*

%files devel
%{_includedir}/sndfile.h
%{_includedir}/sndfile.hh
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/sndfile.pc
%{_libdir}/cmake/SndFile/*.cmake

%files doc
%doc AUTHORS CHANGELOG.md README NEWS.OLD
%{_docdir}/%{name}-%{version}/html
