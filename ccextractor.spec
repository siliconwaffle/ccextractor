%bcond_with rust
%global commit 97b381a2b0bee35d3b22411772329eb540ee511b

Name:           ccextractor
Version:        0.94
Release:        %autorelease
Summary:        A closed captions and teletext subtitles extractor for video streams
Group:          Applications/Internet

License:        GPL-2.0-only AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND Unlicense
URL:            https://%{name}.org
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  automake
%if %{with rust}
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  clang
%endif
# Required for later versions of ccextractor
# BuildRequires:  crate(tesseract-sys/default) = 0.6.1
# BuildRequires:  crate(leptonica-sys/default) = 0.4.7
# BuildRequires:  crate(rsmpeg/ffmpeg6) = 0.14.2
BuildRequires:  gcc
BuildRequires:  make
# BuildRequires:  pkgconfig(glew)
# BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gpac)
BuildRequires:  pkgconfig(lept)
BuildRequires:  pkgconfig(libavcodec)
# BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(tesseract)
BuildRequires:  R(tesseract)

%description
CCExtractor is a software that extracts closed captions from videos of various
formats, even live video streams. Available as a multi-platform desktop
application.

%prep
%autosetup -n %{name}-%{version}/%{_os}
%{__sed} -i "s/commit=(\`git rev-parse HEAD 2>\/dev\/null\`)/commit=%{commit}/g" pre-build.sh

%build
%{_bindir}/autoupdate
./autogen.sh
CFLAGS='%{build_cflags} -Wmaybe-uninitialized'
CXXFLAGS='%{build_cxxflags} -Wmaybe-uninitialized'
LDFLAGS='%{build_ldflags} -Wmaybe-uninitialized'
%configure --enable-ocr --enable-hardsubx --with-rust=no
%make_build

%install
%make_install

%files
%license ../LICENSE.txt
%doc ../docs/*
%{_bindir}/%{name}

%changelog
* Thu Aug 22 2024 Jonathon Hyde <siliconwaffle@trilbyproject.org> - 0.94-1
- Initial RPM Release
