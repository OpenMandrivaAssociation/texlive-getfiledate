# revision 16189
# category Package
# catalog-ctan /macros/latex/contrib/getfiledate
# catalog-date 2009-11-26 14:59:55 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-getfiledate
Version:	1.2
Release:	1
Summary:	Find the date of last modification of a file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/getfiledate
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/getfiledate.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/getfiledate.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package fetches from the system the date of last
modification or opening of an existing file, using the function
\pdffilemoddate (present in recent versions of PDFTeX); the
user may specify how the date is to be presented.

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
%{_texmfdistdir}/tex/latex/getfiledate/getfiledate.sty
%doc %{_texmfdistdir}/doc/latex/getfiledate/README
%doc %{_texmfdistdir}/doc/latex/getfiledate/getfiledate-guide.pdf
%doc %{_texmfdistdir}/doc/latex/getfiledate/getfiledate-guide.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
