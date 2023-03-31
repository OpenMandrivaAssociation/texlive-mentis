Name:		texlive-mentis
Version:	15878
Release:	2
Summary:	A basis for books to be published by Mentis publishers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mentis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mentis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mentis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mentis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX class loads scrbook and provides changes necessary
for publishing at Mentis publishers in Paderborn, Germany. It
is not an official Mentis class, merely one developed by an
author in close co-operation with Mentis.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mentis/mentis.cls
%doc %{_texmfdistdir}/doc/latex/mentis/README
%doc %{_texmfdistdir}/doc/latex/mentis/mentis.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mentis/mentis.dtx
%doc %{_texmfdistdir}/source/latex/mentis/mentis.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
