# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/mentis
# catalog-date 2007-01-09 22:36:10 +0100
# catalog-license lppl
# catalog-version 1.5
Name:		texlive-mentis
Version:	1.5
Release:	1
Summary:	A basis for books to be published by Mentis publishers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mentis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mentis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mentis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mentis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This LaTeX class loads scrbook and provides changes necessary
for publishing at Mentis publishers in Paderborn, Germany. It
is not an official Mentis class, merely one developed by an
author in close co-operation with Mentis.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mentis/mentis.cls
%doc %{_texmfdistdir}/doc/latex/mentis/README
%doc %{_texmfdistdir}/doc/latex/mentis/mentis.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mentis/mentis.dtx
%doc %{_texmfdistdir}/source/latex/mentis/mentis.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
